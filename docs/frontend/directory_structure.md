# Directory Structure for Frontend
All source code of frontend and backend is seperated in two seperate 
directories: `src` and `frontend`.

The overall structure of the frontend directory is given below:

+ frontend
    + static
        + client
            + css
            + img
            + js
        + customadmin
            + css
            + img
            + js
    + templates
        + client
            + includes
        + customadmin
            + includes
        + includes
        + base.html
        + landing.html

The basic directories are static and templates. The static directory consists
of css files, images or assets and js files. While the template directory 
consists of only templates or html files.

Both directories are seperated as per the user level which is client specifies
normal users and customadmin specifies admin users. This can further be 
seperated into different modules in the future depending on the type if pages
that we want to make.

Each module (customadmin and client) has to have a css dir, img dir and js dir.
Those directories holds the respective files used in the templates.

In templates directory, the mose basic `base.html` and `landing.html` files
are kept directly under it as seen above. Then the user specific files are kept
under specific users directory. Like in static, we have also divided it into
modules specific to the type of users i.e. client and customadmin as can be
seen above.

Each modules consists of an includes directory that can be used to include
repetitive code such as navbar or footer or forms and be used in the main 
template using the `{% includes 'dir_name/includes/file.html' %}` syntax.

The includes directory directly under tempates is the basic includes directory
that holds codes that are used all over the project. Such as navbar and footer.
Those codes that are repetitive for a specific user type is to be included in
the modules includes section.
