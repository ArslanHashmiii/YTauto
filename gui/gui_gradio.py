import gradio as gr

from gui.content_automation_ui import GradioContentAutomationUI
from gui.ui_abstract_base import AbstractBaseUI
from gui.ui_components_html import GradioComponentsHTML
from gui.ui_tab_asset_library import AssetLibrary
from gui.ui_tab_config import ConfigUI
from YTauto.utils.cli import CLI


class YTautoUI(AbstractBaseUI):
    '''Class for the GUI. This class is responsible for creating the UI and launching the server.'''

    def __init__(self, colab=False):
        super().__init__(ui_name='gradio_YTauto')
        self.colab = colab
        CLI.display_header()

    def create_interface(self):
        '''Create Gradio interface'''
        with gr.Blocks(theme=gr.themes.Default(spacing_size=gr.themes.sizes.spacing_sm), css="footer {visibility: hidden}", title="YTauto Demo") as YTautoUI:
            with gr.Row(variant='compact'):
                gr.HTML(GradioComponentsHTML.get_html_header())

            self.content_automation = GradioContentAutomationUI(YTautoUI).create_ui()
            self.asset_library_ui = AssetLibrary().create_ui()
            self.config_ui = ConfigUI().create_ui()
        return YTautoUI

    def launch(self):
        '''Launch the server'''
        YTautoUI = self.create_interface()
        if not getattr(self, 'colab', False):
                    print("\n\n********************* STARTING SHORGPT **********************")
                    print("\nYTauto is running here 👉 http://localhost:31415\n")
                    print("********************* STARTING SHORGPT **********************\n\n")
        YTautoUI.queue().launch(server_port=31415, height=1000, allowed_paths=["public/","videos/","fonts/"], share=self.colab, server_name="0.0.0.0")



if __name__ == "__main__":
    app = YTautoUI()
    app.launch()


import signal

def signal_handler(sig, frame):
    print("Closing Gradio server...")
    import gradio as gr
    gr.close_all()
    exit(0)

signal.signal(signal.SIGINT, signal_handler)