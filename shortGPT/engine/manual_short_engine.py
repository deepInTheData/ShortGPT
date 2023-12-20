from shortGPT.audio.voice_module import VoiceModule
from shortGPT.config.languages import Language
from shortGPT.engine.content_short_engine import ContentShortEngine


class ManualShortEngine(ContentShortEngine):
    def __init__(
        self,
        voiceModule: VoiceModule,
        copywriting_script: str,
        background_video_name: str,
        background_music_name: str,
        short_id="",
        num_images=None,
        watermark=None,
        language: Language = Language.ENGLISH,
    ):
        super().__init__(
            short_id=short_id,
            short_type="manual_shorts",
            background_video_name=background_video_name,
            background_music_name=background_music_name,
            num_images=num_images,
            watermark=watermark,
            language=language,
            voiceModule=voiceModule,
        )

        self.copywriting_script = copywriting_script

    def _generateScript(self):
        """
        Implements Abstract parent method to generate the script for the Facts short.
        """
        self._db_script = self.copywriting_script
