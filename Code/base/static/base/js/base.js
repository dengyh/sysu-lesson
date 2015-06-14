$(document).ready(function(){
    $('select[name="inverse-dropdown"], select[name="inverse-dropdown-optgroup"], select[name="inverse-dropdown-disabled"]').select2({dropdownCssClass: 'select-inverse-dropdown'});

    $('select[name="searchfield"]').select2({dropdownCssClass: 'show-select-search'});
    $('select[name="inverse-dropdown-searchfield"]').select2({dropdownCssClass: 'select-inverse-dropdown show-select-search'});
    $('select[name="course"]').select2({dropdownCssClass: 'select-inverse-dropdown show-select-search'});
});
