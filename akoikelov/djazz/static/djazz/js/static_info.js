$(document).ready(function () {
    if (isAdmin) {
        $('*[sic-enabled]').addClass('sic-editing-field');
    }
});