import React from 'react'
import { Card, Image, Table } from 'semantic-ui-react'

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
					<Image floated="right" size="mini" src={user.img_url} />
				</Table.Cell>
				<Table.Cell>{user.name}</Table.Cell>
				<Table.Cell>{user.user_id}</Table.Cell>
			</Table.Row>
		)
	}
}
