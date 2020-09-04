# My Image Repo application

This application uses Flask & Python to host a local server where you can upload and delete images. The application runs inside a Docker container for consistency. Run the following commands inside a bash terminal to use it.

## Initialize the app

To build & start running the container, run

```bash start.sh```

inside the image-repository directory. This starts the container at **localhost:5050**

To specify a different port, supply the port number as an argument to the command, for example:

```bash start.sh 5051```

runs the app on port 5051.

## Using the app

Choose an image and select 'Upload Image' to upload it to the repository. The image must be .png, .jpeg, .jpg, or .gif. You can upload a maximum of 50 images. The uploaded image will be displayed as a 100x100 icon. To view the image in full size, simply click on it. Clicking the trash icon in the upper right corner deletes the image.

## Stopping the container

To stop the running container, run

```docker stop img.repo```

To restart the container, run

```docker stop img.repo && docker start img.repo```

To remove the container, run

```docker rm img.repo```

after stopping the running container. To delete the image, run

```docker rmi img.repo```

## Making changes to the app

To make changes to the application while the container is running, save the changes and run

```touch uwsgi.ini```

This should update the touch-reload and allow changes to be updated on the app after refreshing.

## Errors?

Please create a new issue to let me know! Thanks fren :)


