let pending=false; export async function pay(){ if(pending) return; pending=true; try { return await submitPayment() } catch(e){ preserveCartAndForm(); throw e } finally { pending=false } }
export const finalTotalVisible=true
