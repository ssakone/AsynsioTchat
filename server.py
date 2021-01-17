import asyncio
from textwrap import dedent

class ConnectionPool:

	def __init__(self):
		self.connection_pool = set()

	def send_welcome_message(self, writer):

		# send welcome message
		message =  dedent(f"""
		===
			(Welcome {writer.nickname}!)
			There are {len(self.connection_pool)-1} user(s) here beside

			Help:
			 -	Type anything to tchat
			 - 	/list will all the connected users
			 - 	/quit will disconnect you
		===
		""")
		writer.write(f"{message}".encode())
		pass 
	def brodcast(self, writer, message):

		# pass general message

		pass 
	def brodcast_user_join(self, writer):

		# called when user join

		pass 
	def brodcast_user_quit(self, writer):

		# called when user quit

		pass 
	def brodcast_new_message(self, writer, message):

		# called for user new message

		pass
	def list_users(self, writer):

		# list of all user in the pool

		pass 
	def add_new_user_to_pool(self, writer):

		# add user to pool

		self.connection_pool.add(writer)
	def remove_user_to_pool(self, writer):

		self.connection_pool.remove(writer)

async def handle_connection(reader, writer):

	writer.write("> Enter nickname: ".encode())

	resp =  await reader.readuntil(b"\n")

	writer.nickname = resp.decode().strip()

	connection_pool.add_new_user_to_pool(writer)
	connection_pool.send_welcome_message(writer)

	await writer.drain()

	writer.close()

	await writer.wait_closed()

async def main():

	server = await asyncio.start_server(handle_connection, "0.0.0.0", 8888)

	async with server:
		await server.serve_forever()

connection_pool = ConnectionPool()
asyncio.run(main())