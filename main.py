import json

class Character:
    def __init__(self, name):
        self.name = name
        self.skills = {}
        self.level = 1
        self.xp = 0
        self.xp_to_next_level = 100

    def add_skill(self, skill_name):
        if skill_name not in self.skills:
            self.skills[skill_name] = 0
        else:
            print(f"{skill_name} already exists!")

    def complete_quest(self, skill_name, xp_gain):
        if skill_name not in self.skills:
            print(f"Skill '{skill_name}' not found. Add it first!")
            return
        
        self.skills[skill_name] += xp_gain
        self.xp += xp_gain
        print(f"Gained {xp_gain} XP in {skill_name}!")
        self.check_level_up()

    def check_level_up(self):
        if self.xp >= self.xp_to_next_level:
            self.level += 1
            self.xp -= self.xp_to_next_level
            self.xp_to_next_level = int(self.xp_to_next_level * 1.2)  # XP needed increases by 20%
            print(f"🎉 Level Up! You are now Level {self.level}!")

    def save_progress(self, filename="progress.json"):
        with open(filename, "w") as f:
            json.dump(self.__dict__, f, indent=4)
        print("Progress saved!")

    def load_progress(self, filename="progress.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.__dict__.update(data)
            print("Progress loaded!")
        except FileNotFoundError:
            print("No saved progress found.")


# Example Usage
player = Character("Hero")
player.add_skill("Charisma")
player.complete_quest("Charisma", 30)
player.complete_quest("Charisma", 50)
player.complete_quest("Charisma", 40)  # Should trigger level-up
player.save_progress()
