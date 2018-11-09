$(document).ready(function () {
    $('*[sic]').addClass('sic-editing-field').each(function (index, obj) {
        $(obj).on('click', function () {
            var currentValue = $(obj).text();

            var modal = new tingle.modal({
                footer: true,
                stickyFooter: true,
                closeMethods: ['overlay', 'button', 'escape'],
                cssClass: ['sic-modal']
            });

            modal.addFooterBtn(saveBtnLbl, 'tingle-btn tingle-btn--default', function () {
                var form = $('form.sicUpdateForm', $(this).parent().parent());
                var model = $(obj).attr('sic');
                var value = $('textarea', form).val();

                $.ajax({
                    method: $(form).attr('method'),
                    url: $(form).attr('action'),
                    data: {
                        field_name: model,
                        value: value
                    },
                    dataType: 'json',
                    success: function (data) {
                        $(obj).text(data.value);
                        modal.close();
                    },
                    error: function () {

                    }
                })
            });

            var modalContent = '<form method="post" class="sicUpdateForm" action="{action}">' +
                '<textarea class="sic-textarea" rows="8" placeholder="{ph}">{val}</textarea></form>';

            modalContent = modalContent.replace('{action}', endpointUrl).replace('{ph}', textareaPlaceholder)
                                .replace('{val}', currentValue);

            modal.setContent(modalContent);
            modal.open();
        })
    });
});