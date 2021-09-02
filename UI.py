import pgpy
import PySimpleGUIQt as sg
	
def main():
	sg.theme('DefaultNoMoreNagging')

	gpg_raw = [
		[sg.Multiline(key='encrypted_gpg', size=(None, 150))],
		[
			sg.Button('解密', size=(8, 0.8)),
			sg.Button('清除GPG', size=(8, 0.8)),
			sg.Text('密碼*', size=(4, 0.8)),
			sg.Input(key='decode_pass', size=(15, 0.8), password_char='*')
		]
	]

	txt_raw = [
		[sg.Multiline(key='decrypted_txt', size=(None, 150))],
		[
			sg.Button('加密', size=(8, 0.8)),
			sg.Button('清除文字', size=(8, 0.8)),
			sg.Text('密碼*', size=(4, 0.8)),
			sg.Input(key='encode_pass', size=(15, 0.8), password_char='*')
		]
	]
	
	layout = [
		[sg.Frame('文字訊息', layout=txt_raw), sg.Frame('GPG/PGP訊息', layout=gpg_raw)]
	]

	window = sg.Window(title='加密/解密 - Anonymous Asia 訊息工具 ', icon='win_icon.ico', size=(500, 800), layout=layout)
	while True:
		events, values = window.read()
		if events == sg.WINDOW_CLOSED:
			break

		decode_str = values['encrypted_gpg']
		passh = values['decode_pass']
		gpg_content = values['encrypted_gpg']
		if events == '解密':
			if gpg_content == '' or gpg_content is None:
				sg.popup_error('警告', '未輸入GPG訊息!', background_color='yellow', keep_on_top=True)
			elif passh == '' or passh is None:
				sg.popup_error('警告', '未輸入密碼!', background_color='yellow', keep_on_top=True)
			else:
				dec = pgpy.PGPMessage.from_blob(decode_str)
				try:
					decrypt = dec.decrypt(passh)
					window['decrypted_txt'].update(decrypt.message)
				except pgpy.errors.PGPDecryptionError:
					sg.popup_error('警告', '密碼錯誤!', background_color='yellow', keep_on_top=True)

		encod_str = values['decrypted_txt']
		passh = values['encode_pass']
		text_content = values['decrypted_txt']
		if events == '加密':
			if text_content == '' or text_content is None:
				sg.popup_error('警告', '未輸入訊息內容!', background_color='yellow', keep_on_top=True)
			elif passh == '' or passh is None:
				sg.popup_error('警告', '密碼不能為空! 請輸入下方密碼', background_color='yellow', keep_on_top=True)
			else:
				enc = pgpy.PGPMessage.new(str(encod_str))
				try:
					encode_result = enc.encrypt(passh)
					window['encrypted_gpg'].update(encode_result)
				except pgpy.errors.PGPEncryptionError:
					sg.popup_error('警告', '加密出錯,可嘗試其他密碼。', background_color='yellow', keep_on_top=True)
			
		if events == '清除文字':
			window['decrypted_txt'].update('')
			window['encode_pass'].update('')

		if events == '清除GPG':
			window['encrypted_gpg'].update('')
			window['decode_pass'].update('')
		
	window.close()

if __name__ == "__main__":	
	main()
