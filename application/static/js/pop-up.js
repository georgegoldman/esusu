(function pop(){
confirm('testin the javascript file connection '  );
})

function joinGroup(group_id) {
  fetch(`https://esusu-app.herokuapp.com/join_group?group_id=${group_id}`)
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
      fetch(`https://esusu-app.herokuapp.com/leave_group?group_id=${group_id}`)

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
