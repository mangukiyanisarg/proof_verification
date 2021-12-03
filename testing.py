from app import app,db,logging

import proof
import unittest
import json

import io

app.route(proof)

class Flask_Test(unittest.TestCase):

    def setUp(self):
        app.config['Testing'] = True
        # example connections -'sqlite:///C:\\path\\to\\database.db'
        self.db_uri = 'postgresql://postgres:root@localhost:5432/proof_verification'
        app.config ['SQLALCHEMY_DATABASE_URI']=self.db_uri
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['Debug'] = False
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        pass

    # Test User Proof
    def test_user_proof(self):
        url='/user-proof'
        
        # mock_ data
        mock_request_data={'image': ('pan_originapng.png'),
                            "id_type":"PAN"}

        response=self.app.post(url,data=json.dumps(mock_request_data),content_type='multipart/form-data')
        self.assertEqual(response.status_code, 200) 
        self.assertEqual(response.object(score),100)
        
if __name__ == "__main__":
    unittest.main()