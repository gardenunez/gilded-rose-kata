from .quality_checkpoints import default_quality_checkpoint


class QualityCheckpointFactory:
    def get_quality_checkpoint(self, item_name):
        return default_quality_checkpoint
