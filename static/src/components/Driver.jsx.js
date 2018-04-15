import React from 'react'
import { Card, Image, Table, Modal, Button } from 'semantic-ui-react'
import UserIncidentTable from './UserIncidentTable.jsx'

const Styles = {
	truncate: {
		whiteSpace: 'nowrap',
		overflow: 'hidden',
		textOverflow: 'ellipsis'
	}
}

export default class Driver extends React.Component {
	constructor(props) {
		super(props)
	}

	render() {
		let user = this.props.data

		return (
			<Table.Row>
				<Table.Cell>
					<Image floated="right" size="mini" src={user.user_image} />
				</Table.Cell>
				<Table.Cell>{user.name}</Table.Cell>
				<Table.Cell>{user.user_id}</Table.Cell>
				<Table.Cell>
					<Modal trigger={<Button>Show Incident Log</Button>}>
						<Modal.Header>
							Incident Log for {user.name}
						</Modal.Header>
						<Modal.Content>
							<UserIncidentTable id={user.user_id} />
						</Modal.Content>
					</Modal>
				</Table.Cell>
			</Table.Row>
		)
	}
}
