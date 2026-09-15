(async()=>{
  try{
    if('serviceWorker' in navigator){
      const regs=await navigator.serviceWorker.getRegistrations();
      await Promise.all(regs.map(r=>r.unregister()));
    }
    if('caches' in window){
      const keys=await caches.keys();
      await Promise.all(keys.map(k=>caches.delete(k)));
    }
  }catch(e){}
  try{
    const r=await fetch('./app.js?fresh='+Date.now(),{cache:'no-store'});
    if(!r.ok) throw new Error('app.js non disponibile');
    const code=await r.text();
    (0,eval)(code);
  }catch(e){
    const a=document.getElementById('app');
    if(a)a.innerHTML='<section class="screen active"><div class="wrap"><div class="hero"><div class="logo">🦸‍♂️</div><h1>MARVEL EXPERIENCE</h1><p>Errore di caricamento</p></div><div class="card"><h3>Ricarica la pagina</h3><p class="muted">Il catalogo non è stato caricato. Chiudi questa scheda e riaprila.</p></div></div></section>';
    console.error(e);
  }
})();
