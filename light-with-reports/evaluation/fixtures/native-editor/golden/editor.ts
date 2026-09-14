export const commands = { undo(){}, redo(){}, save(){} }
export function confirmClose(dirty:boolean){ return dirty ? "prompt" : "close" }
export function inspectorFor(selection:string|null){ return selection ? "contextual" : "empty" }
