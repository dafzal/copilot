import React from 'react'
import Driver from './Driver.jsx'
import { Segment, Header, Table } from 'semantic-ui-react'

const Styles = {
	divider: {
		height: 40,
		backgroundColor: '#F6F6F6'
	},
	date: {
		position: 'relative',
		left: 40,
		top: 10,
		fontWeight: 'bold'
	},
	table: {
		position: 'relative',
		left: 40
	}
}

export default class DriverTable extends React.Component {
	constructor(props) {
		super(props)
	}

	render() {
		return (
			<div>
				<div style={Styles.divider}>
					<span style={Styles.date}> Drivers </span>
				</div>
				<div style={Styles.table}>
					<Table
						basic="very"
						collapsing
						singleLine
						selectable
						fixed
						textAlign="left"
					>
						<Table.Header>
							<Table.Row>
								<Table.HeaderCell />
								<Table.HeaderCell>Name</Table.HeaderCell>
								<Table.HeaderCell>Driver ID</Table.HeaderCell>
							</Table.Row>
						</Table.Header>

						<Table.Body>
							{this.props.data.map(row => (
								<Driver data={row} id={row.user_id} />
							))}
						</Table.Body>
					</Table>
				</div>
			</div>
		)
	}
}
