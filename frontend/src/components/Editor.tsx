import {useEffect,useMemo,useRef,useState} from 'react';
import type {DocumentItem,Version} from '../services/api';

export type SaveState='saved'|'dirty'|'saving'|'conflict'|'error';
const escapeHtml=(value:string)=>value.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
export function markdownToHtml(source:string){
  const safe=escapeHtml(source||'').replace(/\r\n/g,'\n'); const lines=safe.split('\n'); let html=''; let inUl=false; let inOl=false;
  const close=()=>{if(inUl){html+='</ul>';inUl=false}if(inOl){html+='</ol>';inOl=false}};
  for(const line of lines){
    if(/^\s*[-*]\s+/.test(line)){if(!inUl){close();html+='<ul>';inUl=true}html+='<li>'+inline(line.replace(/^\s*[-*]\s+/,''))+'</li>';continue}
    if(/^\s*\d+[.)]\s+/.test(line)){if(!inOl){close();html+='<ol>';inOl=true}html+='<li>'+inline(line.replace(/^\s*\d+[.)]\s+/,''))+'</li>';continue}
    close(); if(!line.trim()){html+='<p><br></p>';continue}
    if(/^###\s+/.test(line)){html+='<h3>'+inline(line.replace(/^###\s+/,''))+'</h3>';continue}
    if(/^##\s+/.test(line)){html+='<h2>'+inline(line.replace(/^##\s+/,''))+'</h2>';continue}
    if(/^#\s+/.test(line)){html+='<h1>'+inline(line.replace(/^#\s+/,''))+'</h1>';continue}
    if(/^>\s+/.test(line)){html+='<blockquote>'+inline(line.replace(/^>\s+/,''))+'</blockquote>';continue}
    if(/^\|.+\|$/.test(line)){html+='<pre class="md-table">'+line+'</pre>';continue}
    html+='<p>'+inline(line)+'</p>';
  } close(); return html||'<p><br></p>';
}
function inline(value:string){return value.replace(/\[([^\]]+)\]\((https?:\/\/[^\s)]+)\)/g,'<a href="$2" target="_blank" rel="noreferrer">$1</a>').replace(/\*\*([^*]+)\*\*/g,'<strong>$1</strong>').replace(/__([^_]+)__/g,'<strong>$1</strong>').replace(/\*([^*]+)\*/g,'<em>$1</em>').replace(/_([^_]+)_/g,'<em>$1</em>').replace(/~~([^~]+)~~/g,'<s>$1</s>');}
function draftKey(id:string){return 'kzdoc:draft:'+id}
function toolbarInsert(value:string,start:number,end:number,text:string){const before=text.slice(0,start),selected=text.slice(start,end),after=text.slice(end);const marker=value.indexOf('$');const next=value.replace('$',selected);return{text:before+next+after,start:start+marker,end:start+marker+(selected||'').length};}
function applyWrap(text:string,start:number,end:number,left:string,right=left){const selected=text.slice(start,end)||'texto';const next=text.slice(0,start)+left+selected+right+text.slice(end);return{text:next,start:start+left.length,end:start+left.length+selected.length};}

export function Editor({document,versions,onSave,onClose,onConflict}:{document:DocumentItem;versions:Version[];onSave:(data:{name:string;document_type:string;content:string;base_version_id:string|null})=>Promise<'saved'|'conflict'>;onClose:()=>void;onConflict:()=>void}){
  const initial=document.content||'';const[name,setName]=useState(document.name);const[type,setType]=useState(document.document_type);const[content,setContent]=useState(initial);const[state,setState]=useState<SaveState>('saved');const[message,setMessage]=useState('Salvo');const[readOnly,setReadOnly]=useState(false);
  const history=useRef<string[]>([initial]),future=useRef<string[]>([]),timer=useRef<number|undefined>();const textarea=useRef<HTMLTextAreaElement>(null);
  const draft=useMemo(()=>{try{return localStorage.getItem(draftKey(document.id))}catch{return null}},[document.id]);
  useEffect(()=>{if(draft!==null&&draft!==initial){setContent(draft);setState('dirty');setMessage('Rascunho local recuperado')}},[draft,initial]);
  useEffect(()=>{const saveDraft=()=>{if(state!=='saved'){try{localStorage.setItem(draftKey(document.id),content)}catch{}}};document.addEventListener('visibilitychange',saveDraft);return()=>document.removeEventListener('visibilitychange',saveDraft)},[content,state,document.id]);
  useEffect(()=>{const before=(e:BeforeUnloadEvent)=>{if(state==='dirty'||state==='saving'||state==='conflict'){e.preventDefault();e.returnValue=true}};window.addEventListener('beforeunload',before);return()=>window.removeEventListener('beforeunload',before)},[state]);
  useEffect(()=>()=>{if(timer.current)window.clearTimeout(timer.current)},[]);
  function change(next:string){setContent(next);setState('dirty');setMessage('Alterações não salvas');future.current=[];const h=history.current;if(h[h.length-1]!==next){h.push(next);if(h.length>80)h.shift()}}
  function selection(){const el=textarea.current;return{start:el?.selectionStart||0,end:el?.selectionEnd||0}}
  function insert(value:string){const{start,end}=selection();const r=toolbarInsert(value,start,end,content);change(r.text);requestAnimationFrame(()=>{textarea.current?.focus();textarea.current?.setSelectionRange(r.start,r.end)})}
  function wrap(left:string,right=left){const{start,end}=selection();const r=applyWrap(content,start,end,left,right);change(r.text);requestAnimationFrame(()=>{textarea.current?.focus();textarea.current?.setSelectionRange(r.start,r.end)})}
  function command(cmd:string){if(cmd==='bold')wrap('**');else if(cmd==='italic')wrap('*');else if(cmd==='strike')wrap('~~');else if(cmd==='h1')insert('# $\n');else if(cmd==='h2')insert('## $\n');else if(cmd==='h3')insert('### $\n');else if(cmd==='ul')insert('- $\n');else if(cmd==='ol')insert('1. $\n');else if(cmd==='quote')insert('> $\n');else if(cmd==='code')wrap(String.fromCharCode(96));else if(cmd==='link'){const url=window.prompt('URL do link:','https://');if(url)insert('[$]('+url+')')}else if(cmd==='table')insert('| Coluna 1 | Coluna 2 |\n| --- | --- |\n| $ | Valor |\n');}
  function undo(){if(history.current.length<2)return;const current=history.current.pop()!;future.current.push(current);setContent(history.current[history.current.length-1]);setState('dirty');setMessage('Alterações não salvas')}
  function redo(){const next=future.current.pop();if(!next)return;history.current.push(next);setContent(next);setState('dirty');setMessage('Alterações não salvas')}
  async function save(){if(readOnly||state==='saving')return;setState('saving');setMessage('Salvando…');try{const result=await onSave({name,type,content,base_version_id:document.current_version_id});if(result==='conflict'){setState('conflict');setMessage('Conflito: o documento foi alterado em outra sessão');onConflict();return}try{localStorage.removeItem(draftKey(document.id))}catch{}history.current=[content];future.current=[];setState('saved');setMessage('Salvo agora')}catch{try{localStorage.setItem(draftKey(document.id),content)}catch{}setState('error');setMessage('Falha ao salvar. O rascunho local foi preservado.')}}
  useEffect(()=>{if(state!=='dirty')return;if(timer.current)window.clearTimeout(timer.current);timer.current=window.setTimeout(()=>{void save()},1400)},[content,name,type]);
  const toolbar=[['bold','B','Negrito'],['italic','I','Itálico'],['strike','S','Riscado'],['h1','H1','Título 1'],['h2','H2','Título 2'],['h3','H3','Título 3'],['ul','•','Lista'],['ol','1.','Lista numerada'],['quote','❯','Citação'],['code','<>','Código'],['link','↗','Link'],['table','▦','Tabela']];
  return <section className="editor-workspace">
    <header className="editor-head"><div><div className="editor-breadcrumb">DOCUMENTO / EDIÇÃO</div><input className="editor-title" value={name} onChange={e=>{setName(e.target.value);setState('dirty');setMessage('Alterações não salvas')}}/><div className={'save-state '+state}><span className="save-dot"/>{message}{versions.length?' · v'+versions[0].version_number:''}</div></div><div className="editor-actions"><button className="editor-secondary" onClick={()=>setReadOnly(!readOnly)}>{readOnly?'Editar':'Somente leitura'}</button><button className="editor-secondary" onClick={onClose}>Sair</button><button className="editor-save" disabled={state==='saving'||readOnly} onClick={()=>void save()}>Salvar</button></div></header>
    {!readOnly&&<div className="editor-toolbar">{toolbar.map(([cmd,label,title])=><button type="button" key={cmd} title={title} onMouseDown={e=>e.preventDefault()} onClick={()=>command(cmd)}>{label}</button>)}<span className="toolbar-separator"/><button type="button" onClick={undo} disabled={history.current.length<2} title="Desfazer">↶</button><button type="button" onClick={redo} disabled={!future.current.length} title="Refazer">↷</button></div>}
    <div className="editor-info"><span>{type.toUpperCase()}</span><span>{content.length.toLocaleString('pt-BR')} caracteres</span><span>{state==='saved'?'Sincronizado':state==='saving'?'Sincronizando':state==='conflict'?'Conflito detectado':'Alterações locais'}</span></div>
    <div className={'editor-body '+(readOnly?'readonly':'')}><textarea ref={textarea} value={content} readOnly={readOnly} onChange={e=>change(e.target.value)} spellCheck aria-label="Conteúdo do documento"/><aside className="editor-side"><strong>Documento</strong><label>Tipo<select value={type} onChange={e=>{setType(e.target.value);setState('dirty')}} disabled={readOnly}><option value="txt">Texto</option><option value="md">Markdown</option><option value="doc">Documento</option></select></label><div><span>Versão atual</span><strong>{versions[0]?.version_number||'1'}</strong></div><div><span>Última alteração</span><strong>{new Date(document.updated_at).toLocaleString('pt-BR')}</strong></div><div><span>Proteção</span><strong>Rascunho local ativo</strong></div></aside></div>
    <footer className="editor-foot"><span>Desfazer/refazer pelo editor · alterações locais preservadas em caso de interrupção.</span><span>{readOnly?'MODO SOMENTE LEITURA':'MODO EDIÇÃO'}</span></footer>
  </section>
}
