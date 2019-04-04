import React from "react";

class Listing extends React.Component {

    state = {
        data: [],
        loaded: false,
        placeholder: "Loading..."
    };

    createTable(data){
        return (
            <div classname="table">
                <table classname="table is-striped">
                    <tr>
                        {Object.entries(data)}
                    </tr>
                
                </table>



            </div>








        ) 
    }

    componentDidMount() {
        fetch("api/property")
        .then(response => {
            if (response.status !== 200) {
              return this.setState({ placeholder: "Something went wrong" });
            }
            return response.json();
          })
          .then(data => this.setState({ data: data, loaded: true }));
    }

    render() {
        const { data, loaded, placeholder} = this.state;
        return loaded ? this.createTable(data) : <p>{placeholder}</p>
    }


}

export default Listing;