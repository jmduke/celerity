In general, this thing needs to be tested for any sort of edge cases since it's been mainly my tool (and, along those lines, error handling is atrocious).  Beyond that, I'm working to expand functionality without getting too bloated.

Goals:

- Easier/more 'correct' way to delineate files besides FILE_DELINEATOR schema 
- Piping from STDIN
- Better way to do returning? Are status codes the way to go?
- Better input validation
- Uploading entire directories

Errors:

- What happens with no connection?
