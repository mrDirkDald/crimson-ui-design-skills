export function guard(status:number){ if(status===401) return "/reauth"; if(status===403) return "/forbidden"; if(status===404) return "/not-found"; if(status>=500) return "/server-error"; return "/app" }
export const preserveIntendedRoute = true
