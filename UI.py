import pgpy, pyautogui
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WINDOW_CLOSED
	
def main():
	right_click_menu = ['MENU', ['---', '全選', '複製','貼上']]
	
	layout = [
		[sg.Text('貼上PGP/GPG字段,注意Enter換行!!!')],
		[sg.Multiline(size=(100, 20), key='encrypted_gpg', right_click_menu=right_click_menu)],
		[sg.Button('解密'), sg.Button('清除GPG'), sg.Text('密碼*'), sg.Input(key='decode_pass', password_char='*'), sg.Text('*解密內容會顯示於下方*')],
		[sg.Text('輸入文字內容,複製已加密字串,並發報到你的任何平台!(小心公開你的密碼)\n注意輸入字源限制,例如Twitter有字數限額')],
		[sg.Multiline(size=(100, 20), key='decrypted_txt', right_click_menu=right_click_menu)],
		[sg.Button('加密'), sg.Button('清除文字'), sg.Text('密碼*'), sg.Input(key='encode_pass', password_char='*')]
	]

	window = sg.Window(icon='C:\\Users\\user\\Development\\python\\MessageAPP\\win_icon.ico',  title='加密/解密 - Anonymous Asia訊息工具 ', layout=layout)
	while True:
		events, values = window.read()
		if events == WINDOW_CLOSED:
			break

		if events == '解密':
			decode_str = values['encrypted_gpg']
			passh = values['decode_pass']
			if passh == '' or passh == None:
				sg.popup('未輸入密碼!')
			else:
				dec = pgpy.PGPMessage.from_blob(decode_str)
				try:
					decrypt = dec.decrypt(passh)
					result = decrypt.message
					try:
						bys = str(result, encoding='utf-8')
						window['decrypted_txt'].update(bys)
					except:
						window['decrypted_txt'].update(result)
				except pgpy.errors.PGPDecryptionError:
					sg.popup('密碼錯誤!')

		if events == '加密':
			encod_str = values['decrypted_txt']
			passh = values['encode_pass']			
			if passh == '' or passh == None:
				sg.popup('密碼不能為空! 請輸入下方密碼')
			else:
				enc = pgpy.PGPMessage.new(encod_str, encoding='utf-8')
				try:
					encode_result = enc.encrypt(passh)
					window['encrypted_gpg'].update(encode_result)
				except pgpy.errors.PGPEncryptionError:
					sg.popup('加密出錯,可嘗試其他密碼。')
			
		if events == '清除文字':
			window['decrypted_txt'].update('')
			window['encode_pass'].update('')
		if events == '清除GPG':
			window['encrypted_gpg'].update('')
			window['decode_pass'].update('')
		if events == '全選':
			pyautogui.hotkey('ctrl', 'a')
		if events == '複製':
			pyautogui.hotkey('ctrl', 'c')
		if events == '貼上':
			pyautogui.hotkey('ctrl', 'v')

	window.close()

if __name__ == "__main__":
	sg.theme('DefaultNoMoreNagging')
	main()
