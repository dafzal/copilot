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

export default class DayBox extends React.Component {
	constructor(props) {
		super(props)
	}

	render() {
		return (
			<div>
				<div style={Styles.divider}>
					<span style={Styles.date}> {this.props.date} </span>
				</div>
				<div style={Styles.table}>
					<Table
						basic="very"
						collapsing
						singleLine
						selectable
						color="red"
					>
						<Table.Header>
							<Table.Row>
								<Table.HeaderCell>Time</Table.HeaderCell>
								<Table.HeaderCell>Driver</Table.HeaderCell>
								<Table.HeaderCell>Incident ID</Table.HeaderCell>
								<Table.HeaderCell>Status</Table.HeaderCell>
								<Table.HeaderCell>Issue</Table.HeaderCell>
							</Table.Row>
						</Table.Header>

						<Table.Body>
							{this.props.data.map(row => <Driver data={row} />)}
						</Table.Body>
					</Table>
				</div>
			</div>
		)
	}
}
