$(function() {
    $('.year-option').click(function() {
        $('#year-input').val($(this).attr('data-value'));
        $('#year-span').html($(this).html());
    });

    $('.term-option').click(function() {
        $('#term-input').val($(this).attr('data-value'));
        $('#term-span').html($(this).html());
    });

    $('.type-option').click(function() {
        $('#type-input').val($(this).attr('data-value'));
        $('#type-span').html($(this).html());
    });
});