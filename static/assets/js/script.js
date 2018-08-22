var loc = window.location
var wsStart = "ws://"
if (loc.protocol == "https:"){
    wsStart = "wss://"
}
var webSocketEndpoint =  wsStart + loc.host + loc.pathname  // ws : wss

var socket = new WebSocket(webSocketEndpoint)


socket.onmessage = function(e){
  console.log("message",e)
}

socket.onclose = function(e){
  console.log("close",e)
}

socket.onopen = function(e){
  console.log("opened",e)
}

socket.onerror = function(e){
  console.log("error",e)
}