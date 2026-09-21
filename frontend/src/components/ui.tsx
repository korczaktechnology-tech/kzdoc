import type {ButtonHTMLAttributes, ReactNode} from 'react';

const glyphs:Record<string,string>={home:'⌂',file:'▤',folder:'□',star:'☆',clock:'◷',trash:'⌫',search:'⌕',settings:'⚙',user:'●',plus:'+',image:'▧',video:'▶',more:'•••',grid:'⊞',sign:'✎',scan:'⌗',cloud:'☁'};

export const Icon=({name}:{name:string})=><span className="icon" aria-hidden="true">{glyphs[name]||'•'}</span>;
type ButtonProps=ButtonHTMLAttributes<HTMLButtonElement>&{variant?:string};
export function Button({children,variant='primary',className='',...props}:ButtonProps){return <button className={'button button-'+variant+(className?' '+className:'')} {...props}>{children}</button>}
export function Modal({title,children,onClose}:{title:string;children:ReactNode;onClose:()=>void}){return <div className="modal-backdrop"><section className="modal" role="dialog" aria-modal="true"><header><h2>{title}</h2><button type="button" className="icon-button" onClick={onClose}>×</button></header>{children}</section></div>}
export function StatePanel({title,message}:{title:string;message:string}){return <div className="state-panel"><div className="state-mark">○</div><h3>{title}</h3><p>{message}</p></div>}
