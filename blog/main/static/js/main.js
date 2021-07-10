;(function() {
    $(function() {
        const $el = $('h1');
        $el.append("<div><button class='show-new-text'>Show authors</button></div>");
        const authorsUrl = "http://127.0.0.1/api/v1/authors/";

        const $button = $el.find('.show-new-text');
        const $page_container = $('#page-text');
        const $imgEl = $('#page-text');

        $button.click(function() {
            $.get(authorsUrl, function(data, status){
                $page_container.hide();
                $page_container.empty();
                $.each(data, function(index, value){
                    $page_container.append(`<p>${index} - ${value.name}</p>`);
                })
                $page_container.fadeIn(5000);
            })
        })
    })
})()