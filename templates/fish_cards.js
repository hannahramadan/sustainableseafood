$(`#fave{{fish.fish_id}}`).on('click', (evt) => {
    evt.preventDefault();
    fish_id = $(`#fave{{fish.fish_id}}`).val()
    $.post("favorite_fish/{{fish.fish_id}}", fish_id, (res) =>{
        $(`#fave{{fish.fish_id}}`).html(res)
    });
});

