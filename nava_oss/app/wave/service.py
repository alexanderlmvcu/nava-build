from nava_oss.app.repository import Repository
from nava_oss.app.repository.mongo import MongoRepository
from .schema import WaveformSchema

class Service(object):
 def __init__(self, vid_id, repo_client=Repository(adapter=MongoRepository)):
   self.repo_client = repo_client
   self.vid_id = vid_id

   if not vid_id:
     raise Exception("video id not provided")

 def find_all_waves(self):
   waves  = self.repo_client.find_all({'vid_id': self.vid_id})
   return [self.dump(wave) for wave in waves]

 def find_wave(self, repo_id):
   wave = self.repo_client.find({'vid_id': self.vid_id, 'repo_id': repo_id})
   return self.dump(wave)

 def create_wave_for(self, raspberrySensor):
   self.repo_client.create(self.prepare_wave(raspberrySensor))
   return self.dump(raspberrySensor.data)

 def update_wave_with(self, repo_id, raspberrySensor):
   records_affected = self.repo_client.update({'vid_id': self.vid_id, 'repo_id': repo_id}, self.prepare_wave(raspberrySensor))
   return records_affected > 0

 def delete_wave_for(self, repo_id):
   records_affected = self.repo_client.delete({'vid_id': self.vid_id, 'repo_id': repo_id})
   return records_affected > 0

 def dump(self, data):
   return WaveformSchema(exclude=['_id']).dump(data).data

 def prepare_wave(self, raspberrySensor):
   data = raspberrySensor.data
   data['vid_id'] = self.vid_id
   return data