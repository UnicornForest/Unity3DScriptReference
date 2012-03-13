# written by Jacob Pennock (www.jacobpennock.com)
# based on WordPress Codex Search Plugin by Matthias Krok (www.welovewordpress.de)

# available commands
#   unity_reference_open_selection
#   unity_reference_search_selection
#   unity_reference_search_from_input

import sublime
import sublime_plugin

import subprocess
import webbrowser

def SearchUnityScriptReferenceFor(text):
    url = 'http://unity3d.com/support/documentation/ScriptReference/30_search.html?q=' + text.replace(' ','%20')
    webbrowser.open_new_tab(url)

def OpenUnityFunctionReference(text):
    url = 'http://unity3d.com/support/documentation/ScriptReference/' + text.replace(' ','%20')
    webbrowser.open_new_tab(url)

class UnityReferenceOpenSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            # if the user didn't select anything, search the currently highlighted word
            if selection.empty():
                selection = self.view.word(selection)

            text = self.view.substr(selection)
            OpenUnityFunctionReference(text)

class UnityReferenceSearchSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            # if the user didn't select anything, search the currently highlighted word
            if selection.empty():
                selection = self.view.word(selection)

            text = self.view.substr(selection)            
            SearchUnityScriptReferenceFor(text)

class UnityReferenceSearchFromInputCommand(sublime_plugin.WindowCommand):
    def run(self):
        # Get the search item
        self.window.show_input_panel('Search Unity Refference for', '',
            self.on_done, self.on_change, self.on_cancel)
    def on_done(self, input):
        SearchUnityScriptReferenceFor(input)

    def on_change(self, input):
        pass

    def on_cancel(self):
        pass