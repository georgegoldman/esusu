
function joinGroup(group_id) {
  
  var group_id = group_id;
  
  var entry = {
    group_id: group_id
  };

  fetch(`${window.origin}/join_group`, {
    method: "POST",
    credentials: "include",
    body: JSON.stringify(entry),
    cache: "no cache",
    headers: new Headers({
      "content-type": "application/json"
    })
  })
  

}

function leaveGroup(group_id, user_id, member_id) {

  if (user_id == member_id){
    y = confirm('Click ok to confirm leave');
    y;
    if (y == true){
      fetch(`http://esusu-app.herokuapp.com/leave_group?group_id=${group_id}`)

        .then(res => {
          return res.text()
        ;
        })
        .then(data => {
          data = JSON.parse(data)
          if (data["error"] === "0") {
            alert(data["message"])
          }
        })
    }

  }
  else{
    confirm('Leave rights to members only.');
  }

}
