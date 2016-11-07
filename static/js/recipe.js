/**
 * Created by sachin on 11/5/2016.
 */

jQuery(document).ready(function($){

  $(".recipeDelete").click(function(){


      var recipeid=($(this).closest("tr").attr('id'));



      if(recipeid && confirm("Are you sure you want to delete this recipe?")) {


          $.ajax({

              type: 'POST',
              url: "/recipe/delete",


              data: {
                  id: recipeid,

              },


              success: function (data) {


                  window.location=$(location).attr('href');


              }


          }); //end ajax

      }
  });


});