import {beforeEach,describe,expect,it,vi} from 'vitest';
import {ApiError,api,clearToken,saveSession,getToken} from './services/api';

describe('Fase 13 — integração do cliente HTTP',()=>{
  beforeEach(()=>{
    vi.restoreAllMocks();
    const data=new Map<string,string>();
    Object.defineProperty(globalThis,'localStorage',{configurable:true,value:{
      getItem:(key:string)=>data.get(key)??null,
      setItem:(key:string,value:string)=>data.set(key,value),
      removeItem:(key:string)=>data.delete(key),
      clear:()=>data.clear()
    }});
  });

  it('envia a sessão e codifica identificadores de recursos',async()=>{
    saveSession({token:'sessao-teste',expires_at:'',user:{} as never});
    const fetchMock=vi.spyOn(globalThis,'fetch').mockResolvedValue(
      new Response(JSON.stringify({id:'doc',name:'Teste'}),{status:200,headers:{'Content-Type':'application/json'}})
    );
    await api.document('pasta/documento');
    expect(fetchMock).toHaveBeenCalledTimes(1);
    const [url,options]=fetchMock.mock.calls[0];
    expect(String(url)).toContain('/api/v1/documents/pasta%2Fdocumento');
    expect((options?.headers as Headers).get('Authorization')).toBe('Bearer sessao-teste');
  });

  it('converte respostas HTTP em ApiError e limpa sessão em 401',async()=>{
    saveSession({token:'sessao-expirada',expires_at:'',user:{} as never});
    vi.spyOn(globalThis,'fetch').mockResolvedValue(
      new Response(JSON.stringify({error:{message:'Sessão expirada',code:'unauthorized'}}),{status:401,headers:{'Content-Type':'application/json'}})
    );
    await expect(api.me()).rejects.toMatchObject({status:401,code:'unauthorized'});
    expect(getToken()).toBeNull();
  });

  it('diferencia falha de rede de erro HTTP',async()=>{
    vi.spyOn(globalThis,'fetch').mockRejectedValue(new TypeError('offline'));
    await expect(api.documents()).rejects.toMatchObject({status:0,code:'network_error'});
  });

  it('aceita respostas vazias de operações sem corpo JSON',async()=>{
    vi.spyOn(globalThis,'fetch').mockResolvedValue(new Response('',{status:204}));
    await expect(api.logout()).resolves.toEqual({});
  });

  it('mantém a classe de erro pública para tratamento por status',()=>{
    const error=new ApiError('Conflito',409,'document_conflict');
    expect(error.status).toBe(409);
    expect(error.code).toBe('document_conflict');
  });

  it('remove a sessão explicitamente quando solicitado',()=>{
    saveSession({token:'x',expires_at:'',user:{} as never});
    expect(getToken()).toBe('x');
    clearToken();
    expect(getToken()).toBeNull();
  });
});
