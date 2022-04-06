from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class VendasWindow(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	def admin(self):
		pass

	def sair(self):
		pass

	def add_produto_codigo(self,codigo):
		pass

	def add_produto_nome(self, nome):
		pass

	def atualizar(self):
		pass

	def deletar(self):
		pass

	def pagar(self):
		pass

	def nova_compra(self):
		pass


class VendasApp(App):
	def build(self):
		return VendasWindow()

	




if __name__ == '__main__':
	VendasApp().run()