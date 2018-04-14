import React from 'react'
import {
	Segment,
	Header,
	Image,
	Table,
	Modal,
	Button,
	Input
} from 'semantic-ui-react'
import $ from 'jquery'
import Chart from 'chart.js'

const Styles = {
	truncate: {
		whiteSpace: 'nowrap',
		overflow: 'hidden',
		textOverflow: 'ellipsis'
	}
}

export default class Incident extends React.Component {
	constructor(props) {
		super(props)
		this.input = this.input.bind(this)
		this.submit = this.submit.bind(this)
		this.handleClose = this.handleClose.bind(this)
		this.onOpen = this.onOpen.bind(this)
		this.removeIncident = this.removeIncident.bind(this)
		this.state = {
			issue: '',
			modalOpen: false
		}
	}
	input(e, d) {
		this.setState({ issue: d.value })
	}
	submit() {
		//ajax call to api to send status
		this.props.submit(this.props.data.incident_id, this.state.issue)
		this.setState({ modalOpen: false })
	}
	handleClose() {
		this.setState({ modalOpen: false })
	}
	onOpen() {
		this.setState({ modalOpen: true })
	}

	removeIncident(e, d) {
		$.ajax({
			url: `/resolve_incident`,
			type: 'POST',
			contentType: 'application/json',
			dataType: 'json',
			data: JSON.stringify({
				incident_id: this.props.data.incident_id,
				issue: d.value
			}),
			success: data => {
				console.log('error in submitting resolution')
			},
			error: err => {
				console.error(err)
			}
		})
		this.setState({ modalOpen: false })
	}

	render() {
		let data = this.props.data
		let user = data.user
		return (
			<Table.Row>
				<Table.Cell>{data.timestamp}</Table.Cell>
				<Table.Cell>
					<Header as="h4" image>
						<Image src={data.img_urls[0]} rounded size="mini" />
						<Header.Content>
							{user.name}
							<Header.Subheader>
								<div style={Styles.truncate}>
									{user.user_id}
								</div>
							</Header.Subheader>
						</Header.Content>
					</Header>
				</Table.Cell>
				<Table.Cell>
					<div style={Styles.truncate}>{data.incident_id}</div>
				</Table.Cell>
				<Table.Cell>
					{data.reviewed_at
						? 'Reviewed at ' + data.reviewed_at
						: 'Needs Review'}
				</Table.Cell>
				<Table.Cell>{data.issue ? data.issue : ''}</Table.Cell>
				<Table.Cell>
					<Modal
						open={this.state.modalOpen}
						onClose={this.handleClose}
						trigger={
							<Button
								onClick={this.onOpen}
								basic
								color={
									data.reviewed_at === 'unresolved'
										? 'red'
										: 'green'
								}
							>
								{data.reviewed_at === 'unresolved'
									? 'Review Now'
									: 'See More / Remove'}
							</Button>
						}
					>
						<Modal.Header>Review Incident</Modal.Header>
						<Modal.Content>
							<Image.Group size="small">
								{data.img_urls.map(pic => <Image src={pic} />)}
							</Image.Group>
						</Modal.Content>
						<Modal.Actions>
							<Button onClick={this.removeIncident} value="issue">
								This is a Problem
							</Button>
							<Button
								onClick={this.removeIncident}
								value="notIssue"
							>
								{' '}
								This is not a problem{' '}
							</Button>
						</Modal.Actions>
					</Modal>
				</Table.Cell>
			</Table.Row>
		)
	}
}
