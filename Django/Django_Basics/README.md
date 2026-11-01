# Django Basics

This directory contains laboratory exercises, independent exercises, workshop materials, and practical tasks completed during my introductory Django training.

The course builds on my previous knowledge of Python, relational databases, and the Django ORM. It introduces the main components required to create structured web applications with Django.

## Course Overview

Django Basics introduces the fundamental workflow of a Django web application.

The course begins with project and application setup and continues with URL routing, views, templates, forms, and the connection between incoming HTTP requests and generated HTML responses.

The materials demonstrate how the different parts of a Django application work together:

```text
Browser request
    ↓
URL configuration
    ↓
View
    ↓
Application logic and data
    ↓
Template
    ↓
HTML response
```

## Topics Covered

The main topics covered in this course include:

- Django project structure
- Django applications
- Project configuration
- Development server
- URL routing
- Views
- HTTP requests and responses
- Templates
- Template inheritance
- Template context
- Dynamic content
- Forms
- Form submission
- GET and POST requests
- Basic validation
- Application organization
- Workshop-based development

## Directory Structure

The course materials are organized into topic-based exercise directories.

### Django Introduction

Introductory materials involving:

- Installing Django
- Creating a Django project
- Creating Django applications
- Understanding the project structure
- Configuring installed applications
- Running the development server
- Understanding `manage.py`
- Understanding project settings
- Understanding the role of the main URL configuration

### URLs and Views

Exercises involving:

- Creating URL patterns
- Connecting URLs to views
- Using application-specific URL configurations
- Including application URLs in the project
- Working with path parameters
- Receiving HTTP requests
- Returning HTTP responses
- Separating routing from application behavior

### Templates

Exercises involving:

- Creating HTML templates
- Configuring template directories
- Rendering templates from views
- Passing context data
- Displaying dynamic values
- Using template variables
- Using template tags
- Using template filters
- Organizing reusable page content
- Understanding basic template inheritance

### Workshop

The workshop directory contains a more complete practical application that combines several topics from the course.

The workshop provides experience with:

- Planning a small Django application
- Organizing project files
- Creating URL routes
- Writing views
- Rendering templates
- Passing data to templates
- Connecting multiple pages
- Applying the complete request-response workflow

### Forms Basics

Exercises involving:

- Creating HTML forms
- Receiving user-submitted data
- Understanding GET and POST requests
- Accessing request data in views
- Creating Django forms
- Displaying form fields in templates
- Checking submitted data
- Showing validation errors
- Redisplaying forms after invalid submission
- Processing valid form data

## Django Request-Response Cycle

A central part of the course is understanding how Django processes a browser request.

The basic flow is:

1. The browser sends an HTTP request.
2. Django checks the URL configuration.
3. A matching URL pattern selects a view.
4. The view processes the request.
5. The view may use forms, models, or other application logic.
6. The view renders a template or returns another response.
7. Django sends the HTTP response back to the browser.

Understanding this flow provides the foundation for debugging and building larger Django applications.

## URL Routing

Django URL configurations determine which view should process a particular request.

The course materials provide practice with:

- Project-level URL configuration
- Application-level URL configuration
- The `path()` function
- The `include()` function
- Named URL patterns
- Dynamic URL parameters
- Organizing routes by application

## Views

Views contain the request-handling logic of a Django application.

The exercises introduce views that:

- Receive an `HttpRequest`
- Read request information
- Process application logic
- Pass context to templates
- Render HTML pages
- Return `HttpResponse` objects
- Handle different request methods
- Redirect the user when necessary

## Templates

Templates define the visible HTML output of the application.

The course develops practical experience in:

- Separating Python logic from HTML presentation
- Sending data from views to templates
- Displaying variables
- Using conditions and loops in templates
- Creating reusable page sections
- Building consistent page structures
- Generating dynamic HTML responses

## Forms

Forms provide a structured way to collect and validate user input.

The introductory exercises cover:

- Creating form fields
- Rendering forms
- Submitting data
- Using `request.GET`
- Using `request.POST`
- Checking the request method
- Validating submitted values
- Displaying form errors
- Processing data only after successful validation

These concepts provide the foundation for later work with:

- `forms.Form`
- `forms.ModelForm`
- Model validation
- Create and update workflows
- Authentication forms
- File uploads
- More complex business validation

## Skills Developed

During this stage of my learning journey, I developed practical experience in:

- Creating Django projects and applications
- Understanding Django project structure
- Configuring applications
- Running and testing the development server
- Designing URL patterns
- Connecting URLs to views
- Processing HTTP requests
- Returning HTTP responses
- Rendering HTML templates
- Passing dynamic context data
- Organizing reusable templates
- Creating and processing forms
- Understanding GET and POST requests
- Performing basic input validation
- Following the Django request-response cycle
- Separating routing, application logic, and presentation
- Debugging common Django configuration problems
- Building small multi-page web applications

## Technologies and Tools

- Python 3
- Django
- HTML
- CSS
- SQLite
- PyCharm
- Git
- GitHub
- PowerShell

## Relationship to Previous Courses

Django Basics combines the knowledge developed during the earlier stages of my learning journey.

### Python

Python provides the language fundamentals, functions, classes, modules, and object-oriented programming concepts used throughout Django.

### PostgreSQL

PostgreSQL training provides an understanding of relational databases, tables, keys, constraints, relationships, and SQL queries.

### Python ORM

The Python ORM course introduces Django models, migrations, relationships, QuerySets, and database operations through Python.

### Django Basics

Django Basics combines these areas into web applications that receive browser requests, process application logic, work with data, and return HTML responses.

## Future Development

The concepts introduced in this directory provide a foundation for further Django development, including:

- Advanced forms and ModelForms
- Class-based views
- Authentication
- Authorization
- Custom user interfaces
- Static and media files
- Business logic and service layers
- Testing
- Deployment
- Complete business applications

## Status

**Completed**

This directory is maintained as an educational archive and as a record of my progress in Django web development.

## Navigation

- [Back to Django courses](../)
- [Back to the main repository](../../)