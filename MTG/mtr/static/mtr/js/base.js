$(document).ready(function () {
    $('.burger').click(function (event) {
        $('.burger,.btn-link').toggleClass('active')
        $('body').toggleClass('lock')
    })
    $('.link-s').click(function (event) {
        $('.burger,.btn-link').removeClass('active')
        $('body').removeClass('lock')
    })
    $('.tgl-b').click(function (event) {
        $('.tgl-com').toggleClass('active')
        $('body').toggleClass('lock')

    })
    $('.add-c-bu').click(function (event) {
        $('.tgl-com').removeClass('active')
        $('body').removeClass('lock')

    })


})
