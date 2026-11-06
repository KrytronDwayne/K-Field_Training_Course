/* Native links and browser history remain authoritative. */
function focusFragment(hash) {
  let id;
  try { id=decodeURIComponent(hash.slice(1)); } catch { return; }
  const target=document.getElementById(id);
  if(target)target.focus({preventScroll:true});
}
document.addEventListener('click', event => {
  const a=event.target.closest('a[href^="#"]');
  if(!a)return;
  setTimeout(()=>focusFragment(a.hash),0);
});
if(location.hash)focusFragment(location.hash);
