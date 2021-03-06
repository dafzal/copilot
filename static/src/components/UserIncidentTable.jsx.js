import React from 'react'
import UserIncident from './UserIncident.jsx'
import { Segment, Header, Table } from 'semantic-ui-react'
import $ from 'jquery'

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
		// float: 'none',
		// margin: 0
		// auto
	}
}

export default class UserIncidentTable extends React.Component {
	constructor(props) {
		super(props)
		this.getData = this.getData.bind(this)
		this.state = {
			incidents: []
		}
	}

	getData() {
		$.ajax({
			url: `/incidents`,
			type: 'POST',
			contentType: 'application/json',
			dataType: 'json',
			data: JSON.stringify({
				incident_id: this.props.id
			}),
			success: data => {
				this.setState({ incidents: data })
			},
			error: err => {
				console.error(err)
			}
		})
	}

	render() {
		this.getData()
		return (
			<div style={Styles.table}>
				<Table singleLine selectable textAlign="left">
					<Table.Header>
						<Table.Row>
							<Table.HeaderCell>Time</Table.HeaderCell>
							<Table.HeaderCell>Incident ID</Table.HeaderCell>
							<Table.HeaderCell>Status</Table.HeaderCell>
							<Table.HeaderCell>More</Table.HeaderCell>
						</Table.Row>
					</Table.Header>

					<Table.Body>
						{this.state.incidents.map(inc => (
							<UserIncident data={inc} id={inc.incident_id} />
						))}
					</Table.Body>
				</Table>
			</div>
		)
	}
}
