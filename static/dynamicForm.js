$(document).ready(function(){

   $("button[data-toggle=addset]").click(function() {
        var entrylist = $($(this).closest("div[data-toggle=entry-container]")).find("ul");
        console.log(entrylist);
        var oldentry = entrylist.find("li:last");
        console.log(oldentry);

        // var target = $($(this).data("target"));
        // //console.log(target);
        // var oldrow = target.find("li:last");
        // var newrow = oldrow.clone(true);
        // // console.log(newrow);
        // var oldentrynum = oldrow.data("entrynum");
        // console.log(oldentrynum);
        // var newentrynum = oldentrynum + 1;
        // newrow.attr("data-entrynum", newentrynum);
        // console.log(newrow.data("entrynum"));

        // //newrow.attr('data-id', elem_num);
        // newrow.find(":input").each(function() {
        //     // console.log(this);
        //     var id = $(this).attr('id').replace('entries-' + (oldentrynum) + '-', 'entries-' + (newentrynum) + '-');
        //     $(this).attr('name', id).attr('id', id).val('').removeAttr("checked");
        // });
        // oldrow.after(newrow);
        // console.log(newrow);


   });

   $("button[data-toggle=removeset]").click(function() {
        var target = $($(this).data("target"));
        if(target.find("li").length > 1) {
            var lastrow = target.find("li:last");
            console.log(lastrow);
            lastrow.remove();
        }
   });

   $("button[data-toggle=addexercise]").click(function() {
        var target = $($(this).data("target"));
        console.log(target);
        var oldex = target.find("div[data-toggle=exercise-list]:last");
        var newex = oldex.clone(true);
        console.log(newex);
        oldex.after(newex);

   });
});