from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

class ReportCheckerApp(App):
    def build(self):
        root = ScrollView()
        layout = BoxLayout(orientation='vertical', padding=20, spacing=12, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))

        # Header Title
        layout.add_widget(Label(
            text='[b]High School Report Checker[/b]', 
            markup=True, 
            font_size=20, 
            size_hint_y=None, 
            height=40
        ))

        # Core High School Subjects
        self.inputs = {}
        subjects = ['Mathematics', 'English', 'Kiswahili', 'Biology', 'Chemistry', 'Physics', 'History', 'Geography']
        
        for subj in subjects:
            box = BoxLayout(orientation='horizontal', size_hint_y=None, height=40, spacing=10)
            box.add_widget(Label(text=subj, size_hint_x=0.5))
            text_input = TextInput(
                hint_text='0 - 100', 
                multiline=False, 
                input_filter='float', 
                size_hint_x=0.5
            )
            box.add_widget(text_input)
            self.inputs[subj] = text_input
            layout.add_widget(box)

        # Action Button
        calc_btn = Button(
            text='Check & Calculate Grade', 
            size_hint_y=None, 
            height=50, 
            background_color=(0.1, 0.5, 0.8, 1)
        )
        calc_btn.bind(on_press=self.calculate_results)
        layout.add_widget(calc_btn)

        # Display Result
        self.result_label = Label(
            text='Enter marks above to view results.', 
            markup=True, 
            size_hint_y=None, 
            height=100
        )
        layout.add_widget(self.result_label)

        root.add_widget(layout)
        return root

    def calculate_results(self, instance):
        try:
            total_marks = 0
            count = 0
            
            for subj, widget in self.inputs.items():
                val = widget.text.strip()
                if val:
                    score = float(val)
                    if score < 0 or score > 100:
                        self.result_label.text = f'[color=ff0000]Error: {subj} mark must be 0-100[/color]'
                        return
                    total_marks += score
                    count += 1
            
            if count == 0:
                self.result_label.text = '[color=ff0000]Please enter marks for at least one subject.[/color]'
                return

            mean_score = total_marks / count
            
            # Grading criteria logic
            if mean_score >= 80:
                grade = 'A'
            elif mean_score >= 75:
                grade = 'A-'
            elif mean_score >= 70:
                grade = 'B+'
            elif mean_score >= 65:
                grade = 'B'
            elif mean_score >= 60:
                grade = 'B-'
            elif mean_score >= 55:
                grade = 'C+'
            elif mean_score >= 50:
                grade = 'C'
            elif mean_score >= 45:
                grade = 'C-'
            elif mean_score >= 40:
                grade = 'D+'
            elif mean_score >= 35:
                grade = 'D'
            elif mean_score >= 30:
                grade = 'D-'
            else:
                grade = 'E'
            
            self.result_label.text = (
                f'[color=00ff00]Subjects Entered:[/color] {count}\n'
                f'[color=00ff00]Total Marks:[/color] {total_marks:.1f}\n'
                f'[color=00ff00]Mean Score:[/color] {mean_score:.2f}%\n'
                f'[color=00ff00]Overall Grade:[/color] {grade}'
            )
        except ValueError:
            self.result_label.text = '[color=ff0000]Error: Please enter valid numbers only.[/color]'

if __name__ == '__main__':
    ReportCheckerApp().run()
          
