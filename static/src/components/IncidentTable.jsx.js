import React from 'react'
import Incident from './Incident.jsx'
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
		// position: 'relative'
		float: 'none',
		margin: 0
		// auto
	}
}

export default class IncidentTable extends React.Component {
	constructor(props) {
		super(props)
	}

	render() {
		return (
			<div>
				<div style={Styles.divider}>
					<span style={Styles.date}> Incidents </span>
				</div>
				<div style={Styles.table}>
					<Table singleLine selectable textAlign="left">
						<Table.Header>
							<Table.Row>
								<Table.HeaderCell>Time</Table.HeaderCell>
								<Table.HeaderCell>Driver</Table.HeaderCell>
								<Table.HeaderCell>Incident ID</Table.HeaderCell>
								<Table.HeaderCell>Status</Table.HeaderCell>
								<Table.HeaderCell>Issue</Table.HeaderCell>
								<Table.HeaderCell>More</Table.HeaderCell>
							</Table.Row>
						</Table.Header>

						<Table.Body>
							{this.props.data.map(row => (
								<Incident
									data={row}
									id={row.incident_id}
									submit={this.props.submit}
								/>
							))}
						</Table.Body>
					</Table>
				</div>
			</div>
		)
	}
}
