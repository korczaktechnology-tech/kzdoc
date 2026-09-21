import {describe,expect,it} from 'vitest';
import {clearDraft,draftKey,preserveDraft,recoverDraft,saveWithDraftFallback,type DraftStorage} from './editorPersistence';

function storage():DraftStorage{
  const data=new Map<string,string>();
  return {
    getItem:key=>data.get(key)||null,
    setItem:(key,value)=>{data.set(key,value)},
    removeItem:key=>{data.delete(key)}
  };
}

describe('proteção de rascunho da Fase 8',()=>{
  it('preserva o conteúdo quando o salvamento é interrompido',()=>{
    const s=storage();
    preserveDraft(s,'doc-1','conteúdo que não pode ser perdido');
    expect(recoverDraft(s,'doc-1')).toBe('conteúdo que não pode ser perdido');
  });

  it('remove o rascunho depois de uma confirmação de salvamento',()=>{
    const s=storage();
    preserveDraft(s,'doc-2','salvo');
    clearDraft(s,'doc-2');
    expect(recoverDraft(s,'doc-2')).toBeNull();
    expect(draftKey('doc-2')).toBe('kzdoc:draft:doc-2');
  });

  it('preserva o rascunho quando o salvamento falha',async()=>{
    const s=storage();
    await expect(saveWithDraftFallback(s,'doc-3','conteúdo pendente',async()=>{throw new Error('falha de rede')})).rejects.toThrow('falha de rede');
    expect(recoverDraft(s,'doc-3')).toBe('conteúdo pendente');
  });

  it('preserva o rascunho quando o servidor devolve conflito',async()=>{
    const s=storage();
    const result=await saveWithDraftFallback(s,'doc-4','alteração local',async()=> 'conflict',value=>value==='saved');
    expect(result).toBe('conflict');
    expect(recoverDraft(s,'doc-4')).toBe('alteração local');
  });
});
