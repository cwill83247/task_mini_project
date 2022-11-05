document.addEventListener('DOMContentLoaded', function() {
    let sidenav = document.querySelectorAll('.sidenav');              //renamed variable to sidenav
    M.Sidenav.init(sidenav);                                         //initialising the variable above.. 
 
    //date picker
    let datepicker = document.querySelectorAll('.datepicker');      
    M.Datepicker.init(datepicker, {                                      //documentation for cusotmizing this is on Materialize Page for Pickers > Date
        format: "dd mmmm, yyyy",                                          // this changes the date month year format                                                 
        i18n: {done: "Select" }                                       //i18n is an internationalization std anmd allows us to change a word to something else in this example done becomes Select

    });
    
    //initializing the dropdown option 
    let selects = document.querySelectorAll('select');
    M.FormSelect.init(selects);

  });