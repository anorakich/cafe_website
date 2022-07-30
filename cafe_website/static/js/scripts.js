$(function () {
    $('.like').click(function () {
            var like = $(this)
            if (like.attr('src') == "media/hearths/filled.png") {
                like.attr('src', "media/hearths/shaped.png")
            } else {
                like.attr('src', "media/hearths/filled.png")
            }
        }
    )

})
