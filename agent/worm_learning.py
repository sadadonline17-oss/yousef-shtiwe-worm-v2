import os
import json

class WormLearningLoop:
    def __init__(self, memory_path="~/.yousef_shtiwe/knowledge.json"):
        self.memory_path = os.path.expanduser(memory_path)
        self.success_count = 0

    def worm_learn(self, task_result):
        self.success_count += 1
        if self.success_count >= 3:
            print("[👁] YOUSEF SHTIWE | Learning from experience. Generating new offensive skills...")
            self._analyze_and_store(task_result)
            self.success_count = 0

    def _analyze_and_store(self, data):
        # High-level logic to extract patterns from successful exploits
        knowledge = {"timestamp": "2026-04-15", "new_vector": "Autonomous Discovery"}
        if not os.path.exists(os.path.dirname(self.memory_path)):
            os.makedirs(os.path.dirname(self.memory_path))
        
        with open(self.memory_path, "a") as f:
            f.write(json.dumps(knowledge) + "\n")
