(function pop(){
confirm('testin the javascript file connection '  );
})

function joinGroup(group_id) {
  fetch(`http://localhost:5000/join_group?group_id=${group_id}`)
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

function leaveGroup(group_id, user_id, member_id) {

  if (user_id == member_id){
    y = confirm('Click ok to confirm leave');
    y;
    if (y == true){
      fetch(`http://localhost:5000/leave_group?group_id=${group_id}`)

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
