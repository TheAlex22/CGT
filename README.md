# CGT : composite generator technique!
## How to run it?
1. Install docker
2. clone the repo
3. Navigate to the test generator (to the location of the dockerfile)
4. Execute the following command:
	`docker build -t [Name for the image] .`
5. Check if the image was created in the docker desktop application
6. Create a folder for the output of the test generator
7. Create a package.txt for any dependencies needed for the project
6. Execute the following commands:
  ```
  docker run --rm \
    -v absolute/path/to/project:/input:ro \
    -v absolute/path/to/result:/output \
    -v absolute/path/to/package:/package:ro \
    [Name of your image] \
    --project-path /input \
    --output-path /output \
    --module-name mypackage.mymodule
  ```
  `-v absolute/path/to/project:/input:ro` is the path to the project that you are testing.  
  `-v absolute/path/to/result:/output` is the path to the output folder you made.  
  `-v absolute/path/to/package.txt:/package:ro` is the path to the folder which contains package.txt.  

  After the image you can run normal pynguin commands.

  - NB: If you wish to analise the docker container and it's logs remove the `--rm` tag.
  - NB: Make sure that the folders are accessable to docker


  # Test generator tools used
  ## Pynguin