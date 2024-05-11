# APP-Service
Brief description of the backend project.


### Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Docker on your machine. If not, you can download and install it from [here](https://www.docker.com/products/docker-desktop).

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/your-repo.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd your-repo
   ```

3. **Create a `.env` file:**

   Create a `.env` file in the project root and add your environment variables.
   ```
    MODEL_API=https://jsonplaceholder.typicode.com/posts
    FRONTEND=http://localhost:8080
   
    ```
### Running the Project

To run the project, follow these steps:

1. **Make sure the `.env` file exists:**

   Ensure the `.env` file exists in the project root directory with the necessary environment variables.

2. **Run Docker Compose:**

   ```bash
   docker-compose up
   ```

   This command will start the project and make it accessible at http://localhost:80.

### Stopping the Project

To stop the project, press `Ctrl + C` in the terminal where Docker Compose is running.
