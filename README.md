# my-pub-ip
> Make sure you have Docker installed and that you are in the ROOT folder
1. Build the Docker image locally
   ```shell script
   $ docker build -t lirondadon/my-pub-ip:<tag> .
   ```

2. Run the Docker container with the mandatory env variables
   ```shell script
   $ docker run -it -p 5000:5000 lirondadon/my-pub-ip:<tag>
   ```

3. If no errors appear in the log, the app should run on `http://localhost:5000`

4. Enjoy!
