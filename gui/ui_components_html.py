class GradioComponentsHTML:

    @staticmethod
    def get_html_header() -> str:
        '''Create HTML for the header with "Talk on Mehfil" and GitHub buttons only'''
        return '''
            <style>
                @keyframes blink-border {
                    0% { border-color: deeppink; }
                    50% { border-color: #ffffff; }
                    100% { border-color: deeppink; }
                }
            </style>
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 5px;">
                <h1 style="margin-left: 0px; font-size: 35px;">YTauto</h1>
                <div style="flex-grow: 1; text-align: right;">
                    <a href="http://www.mehfil.arslanhashmi.online/arslanhashmii" target="_blank" style="text-decoration: none;">
                        <button style="margin-right: 10px; padding: 10px 20px; font-size: 16px; color: #fff; background-color: #7289DA; border: 2px solid deeppink; border-radius: 5px; cursor: pointer; transition: transform 0.1s ease; animation: blink-border 1s infinite; font-weight: bold;"
                            onmousedown="this.style.transform='scale(0.95)'"
                            onmouseup="this.style.transform='scale(1)'"
                            onmouseleave="this.style.transform='scale(1)'">
                            Talk on Mehfil
                        </button>
                    </a>
                    <a href="https://github.com/ArslanHashmmiii/YTauto" target="_blank" style="text-decoration: none;">
                        <button style="padding: 10px 20px; font-size: 16px; color: #fff; background-color: #333; border: none; border-radius: 5px; cursor: pointer;">
                            Like the concept? Add a Star on Github 👉 ⭐
                        </button>
                    </a>
                </div>
            </div>
        '''

    @staticmethod
    def get_html_error_template() -> str:
        return '''
        <div style='text-align: center; background: #ff7f7f; color: #a94442; padding: 20px; border-radius: 5px; margin: 10px;'>
          <h2 style='margin: 0; color: black'>ERROR : {error_message}</h2>
          <p style='margin: 10px 0; color: black'>Traceback Info : {stack_trace}</p>
          <p style='margin: 10px 0; color: black'>If the problem persists, don't hesitate to contact our support. We're here to assist you.</p>
          <a href='https://discord.gg/ZhYkPHAm' target='_blank' style='background: #a94442; color: #fff; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; text-decoration: none;'>Get Help on Discord</a>
        </div>
        '''

    @staticmethod
    def get_html_video_template(file_url_path, file_name, width="auto", height="auto"):
        """
        Generate an HTML code snippet for embedding and downloading a video.

        Parameters:
        file_url_path (str): The URL or path to the video file.
        file_name (str): The name of the video file.
        width (str, optional): The width of the video. Defaults to "auto".
        height (str, optional): The height of the video. Defaults to "auto".

        Returns:
        str: The generated HTML code snippet.
        """
        html = f'''
            <div style="display: flex; flex-direction: column; align-items: center;">
                <video width="{width}" height="{height}" style="max-height: 100%;" controls>
                    <source src="{file_url_path}" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
                <a href="{file_url_path}" download="{file_name}" style="margin-top: 10px;">
                    <button style="font-size: 1em; padding: 10px; border: none; cursor: pointer; color: white; background: #007bff;">Download Video</button>
                </a>
            </div>
        '''
        return html
