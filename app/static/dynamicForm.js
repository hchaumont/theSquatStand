$(document).ready(function(){

   $("button[data-toggle=addEntry]").click(function() {
        var entryList = $(this).closest("div[data-toggle=entryContainer]").find("ul");
        //console.log(entryList);
        var oldEntry = entryList.find("li:last");
        //console.log(oldEntry);
        var oldIndex = oldEntry.data("index");
        var newIndex = oldIndex + 1;
        var newEntry = oldEntry.clone(true, true);
        newEntry.data("index", newIndex);
        // console.log(newEntry.data("index"));

        // make sure names and labels are correctly incremented
        newEntry.find("label").each(function() {
            var labelFor = $(this).attr("for");
            // console.log(labelFor);
            $(this).attr("for", labelFor.replace('entries-' + (oldIndex) + "-", 'entries-' + (newIndex) + "-" ));
            // console.log($(this).attr("for"));
        });
        newEntry.find("input").each(function() {
            var id = $(this).attr("id");
            // console.log(id);
            $(this).attr("id", id.replace('entries-' + (oldIndex) + "-", 'entries-' + (newIndex) + "-" ));
            // console.log($(this).attr("id"));
            $(this).attr("name", id.replace('entries-' + (oldIndex) + "-", 'entries-' + (newIndex) + "-" ));
            // console.log($(this).attr("name"));
            $(this).val('');
        });


        oldEntry.after(newEntry);


        // //newrow.attr('data-id', elem_num);
        // newrow.find(":input").each(function() {
        //     // console.log(this);
        //     var id = $(this).attr('id').replace('entries-' + (oldentrynum) + '-', 'entries-' + (newentrynum) + '-');
        //     $(this).attr('name', id).attr('id', id).val('').removeAttr("checked");
        // });
        // oldrow.after(newrow);
        // console.log(newrow);


   });

   $("button[data-toggle=removeEntry]").click(function() {
        var entryList = $(this).closest("div[data-toggle=entryContainer]").find("ul");
        if(entryList.find("li").length > 1) {
            var lastEntry = entryList.find("li:last");
            // console.log(lastEntry.data("index"));
            lastEntry.remove();
        }
   });

   $("button[data-toggle=addExercise]").click(function() {
        var exerciseList = $(this).closest("div[data-toggle=exerciseContainer]");
        var oldExercise = exerciseList.find("div[data-toggle=entryContainer]:last");
        var oldIndex = oldExercise.data("index");
        var newIndex = oldIndex + 1;
        var newExercise = oldExercise.clone(true, true);       
        newExercise.data("index", newIndex);

        newExercise.find("li").slice(1).remove(); // remove all but the first entry

        // Make sure the labels, names, ids are incremented correctly.
        newExercise.find("label").each(function() {
            var labelFor = $(this).attr("for");
            // console.log(labelFor);
            $(this).attr("for", labelFor.replace('exercises-' + (oldIndex) + "-", 'exercises-' + (newIndex) + "-" ));
            // console.log($(this).attr("for"));
        });
        newExercise.find("input").each(function() {
            var id = $(this).attr("id");
            // console.log(id);
            $(this).attr("id", id.replace('exercises-' + (oldIndex) + "-", 'exercises-' + (newIndex) + "-" ));
            // console.log($(this).attr("id"));
            $(this).attr("name", id.replace('exercises-' + (oldIndex) + "-", 'exercises-' + (newIndex) + "-" ));
            // console.log($(this).attr("name"));
            $(this).val('');
        });

        oldExercise.after(newExercise);

        // console.log(target);
        // var oldex = target.find("div[data-toggle=exercise-list]:last");
        // var newex = oldex.clone(true);
        // console.log(newex);
        // oldex.after(newex);

   });

   $("button[data-toggle=removeExercise]").click(function() {
        var exerciseList = $(this).closest("div[data-toggle=exerciseContainer]");
        if(exerciseList.find("div[data-toggle=entryContainer]").length > 1) {
            var lastExercise = exerciseList.find("div[data-toggle=entryContainer]:last");
            lastExercise.remove();
        }
   });
});