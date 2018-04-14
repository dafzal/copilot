import React from 'react'
import { Segment, Header, Image, Table, Modal, Button } from 'semantic-ui-react'

export default class Driver extends React.Component {
	constructor(props) {
		super(props)
	}

	render() {
		return (
			<Table.Row>
				<Table.Cell>06:14</Table.Cell>
				<Table.Cell>
					<Header as="h4" image>
						<Image
							src="https://cdn1.iconfinder.com/data/icons/ninja-things-1/1772/ninja-simple-512.png"
							rounded
							size="mini"
						/>
						<Header.Content>
							{this.props.name}
							<Header.Subheader>UserID</Header.Subheader>
						</Header.Content>
					</Header>
				</Table.Cell>
				<Table.Cell>{this.props.number}</Table.Cell>
				<Table.Cell>
					<Modal trigger={<Button>See More</Button>}>
						<Modal.Header>Select a Photo</Modal.Header>
						<Modal.Content image>
							<Image
								wrapped
								size="medium"
								src="https://cdn1.iconfinder.com/data/icons/ninja-things-1/1772/ninja-simple-512.png"
							/>
							<Modal.Description>
								<Header>Default Profile Image</Header>
								<p>
									We've found the following gravatar image
									associated with your e-mail address.
								</p>
								<p>Is it okay to use this photo?</p>
							</Modal.Description>
						</Modal.Content>
					</Modal>
				</Table.Cell>
			</Table.Row>
		)
	}
}
